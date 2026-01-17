import streamlit as st
import pandas as pd
import os
from email.message import EmailMessage
import ssl
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from PIL import Image
import time
import shutil
import zipfile
from datetime import datetime
from estilos import obtener_estilos_css
from email_template import generar_email_html

# =========================================
# Credenciales desde st.secrets
# =========================================
try:
    redcap_username = st.secrets["redcap_username"]
    redcap_password = st.secrets["redcap_password"]
    email_sender = st.secrets["email_sender"]
    email_password = st.secrets["email_password"]
except Exception as e:
    st.error("❌ Error al cargar los secretos. Por favor configura tus secretos de Streamlit.")
    st.stop()

# =========================================
# Opciones de Chrome
# =========================================
def get_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-software-rasterizer")
    chrome_options.add_argument("--disable-background-timer-throttling")
    chrome_options.add_argument("--disable-backgrounding-occluded-windows")
    chrome_options.add_argument("--disable-renderer-backgrounding")
    chrome_options.add_argument("--disable-features=TranslateUI")
    chrome_options.add_argument("--disable-ipc-flooding-protection")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-sync")
    chrome_options.add_argument("--no-first-run")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-web-security")
    chrome_options.add_argument("--disable-features=VizDisplayCompositor")
    chrome_options.add_argument("--memory-pressure-off")
    chrome_options.add_argument("--max_old_space_size=4096")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument("--log-level=3")
    return chrome_options

# =========================================
# Captura de Pantalla
# =========================================
def download_barcode_images(record_ids, username, password):
    driver = None
    try:
        chrome_options = get_chrome_options()
        folder = "codigos_barras"
        os.makedirs(folder, exist_ok=True)
        
        try:
            driver = webdriver.Chrome(options=chrome_options)
        except Exception as e:
            st.error(f"❌ Fallo al inicializar Chrome: {e}")
            return []
        
        wait = WebDriverWait(driver, 30)
        st.info("🔐 Iniciando sesión en RedCap...")
        url = "https://redcap.prisma.org.pe/redcap_v14.5.11/DataEntry/record_status_dashboard.php?pid=19"
        
        try:
            driver.get(url)
        except Exception as e:
            st.error(f"❌ Fallo al cargar RedCap: {e}")
            return []

        try:
            username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
            username_field.clear()
            username_field.send_keys(username)
            
            password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))
            password_field.clear()
            password_field.send_keys(password)
            password_field.send_keys(Keys.ENTER)
            
            wait.until(EC.url_contains("record_status_dashboard.php"))
            st.success("✅ Sesión iniciada")
        except Exception as e:
            st.error(f"❌ Fallo en inicio de sesión: {e}")
            return []

        TARGET_URL_TEMPLATE = (
            "https://redcap.prisma.org.pe/redcap_v14.5.11/DataEntry/index.php?pid=19&id={id_val}&event_id=59&page=recepcion_de_muestra"
        )

        downloaded_files = []
        progress_bar = st.progress(0)
        total_ids = len(record_ids)
        status_message = st.empty()
        
        for idx, id_val in enumerate(record_ids):
            try:
                status_message.info(f"📸 Procesando Record ID: {id_val} ({idx + 1}/{total_ids})")
                
                target_url = TARGET_URL_TEMPLATE.format(id_val=id_val)
                driver.get(target_url)
                
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table tbody")))

                try:
                    loading_locator = (By.XPATH, "//*[contains(text(),'PIPING DATA')]")
                    WebDriverWait(driver, 5).until(EC.invisibility_of_element_located(loading_locator))
                except TimeoutException:
                    pass

                try:
                    tr_selector = "tr#barcode-tr"
                    tr_el = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, tr_selector)))
                except TimeoutException:
                    st.warning(f"⚠️ Código de barras no encontrado para ID: {id_val}")
                    continue

                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", tr_el)
                time.sleep(1.4)

                screenshot_path = os.path.join(folder, f"Muestra_record_{id_val}.png")
                tr_el.screenshot(screenshot_path)

                try:
                    img = Image.open(screenshot_path)
                    w, h = img.size
                    new_w = int(w * 2 / 3)
                    img_cropped = img.crop((0, 0, new_w, h))
                    img_cropped.save(screenshot_path)
                    downloaded_files.append(screenshot_path)
                except Exception as e:
                    st.error(f"❌ Error al procesar imagen para ID {id_val}: {e}")

            except TimeoutException:
                st.error(f"⏰ Tiempo de espera agotado para Record ID: {id_val}")
            except Exception as e:
                st.error(f"❌ Error al procesar ID {id_val}: {e}")
            
            progress_bar.progress((idx + 1) / total_ids)

        return downloaded_files

    except Exception as e:
        st.error(f"❌ Error en descarga: {e}")
        return []
    
    finally:
        if driver:
            try:
                driver.quit()
            except:
                pass

# =========================================
# Creación de ZIP
# =========================================
def create_zip_file(attachment_files, record_ids):
    try:
        timestamp = datetime.now().strftime("%Y%m%d")
        zip_filename = f"muestras_{timestamp}.zip"
        zip_path = os.path.join("codigos_barras", zip_filename)
        
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in attachment_files:
                if os.path.exists(file_path):
                    filename = os.path.basename(file_path)
                    zipf.write(file_path, filename)
                    
        if os.path.exists(zip_path):
            return zip_path
        else:
            st.error("❌ Fallo al crear ZIP")
            return None
            
    except Exception as e:
        st.error(f"❌ Error al crear ZIP: {e}")
        return None

# =========================================
# Envío de Email
# =========================================
def send_email_with_zip(record_ids, attachment_files, email_receiver):
    try:
        zip_path = create_zip_file(attachment_files, record_ids)
        
        if not zip_path or not os.path.exists(zip_path):
            st.error("❌ No se pudo crear el ZIP")
            return False
        
        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['Subject'] = "🧬 Códigos de Barras | Lab Muestras Humanas - PRESIENTE"

        html_body = generar_email_html(
            total_capturas=len(attachment_files),
            total_records=len(record_ids),
            zip_filename=os.path.basename(zip_path),
            zip_size_mb=os.path.getsize(zip_path) / (1024 * 1024)
        )
       
        em.add_alternative(html_body, subtype="html")

        with open(zip_path, "rb") as f:
            zip_filename = os.path.basename(zip_path)
            em.add_attachment(
                f.read(),
                maintype="application",
                subtype="zip",
                filename=zip_filename
            )

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context, timeout=30) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        return True

    except Exception as e:
        st.error(f"❌ Fallo al enviar email: {e}")
        return False

# =========================================
# Procesamiento CSV
# =========================================
def process_csv_upload():
    st.subheader("📁 Cargar CSV con Record IDs")
    
    with st.expander("📄 Ejemplo de Formato CSV"):
        example_data = pd.DataFrame({"record_id": ["1", "1048", "1049", "1055"]})
        st.dataframe(example_data, use_container_width=True, hide_index=True)
        
        example_csv = example_data.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="📥 Descargar tabla de muestra",
            data=example_csv,
            file_name="tabla_muestra.csv",
            mime="text/csv",
        )
    
    uploaded_file = st.file_uploader("Cargar tu archivo CSV", type=["csv"])
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            if "record_id" not in df.columns:
                st.error("❌ El CSV no contiene 'record_id'.")
                return None
            
            st.subheader("📊 Vista Previa")
            st.dataframe(df.head(10), use_container_width=True, hide_index=True)
            st.info(f"Total de filas: {len(df)}")
            
            df["record_id_numeric"] = pd.to_numeric(df["record_id"], errors="coerce")
            invalid_values = df.loc[df["record_id_numeric"].isnull(), "record_id"]
            
            if not invalid_values.empty:
                st.warning("⚠️ Valores no numéricos encontrados:")
                st.write(invalid_values.tolist())
                st.info("Solo se procesarán valores numéricos válidos.")
            
            valid_df = df.dropna(subset=["record_id_numeric"]).copy()
            
            if len(valid_df) == 0:
                st.error("❌ No se encontraron IDs válidos.")
                return None
            
            valid_df["record_id_int"] = valid_df["record_id_numeric"].astype(int)
            record_ids = valid_df["record_id_int"].tolist()
            
            st.success(f"✅ {len(record_ids)} record IDs válidos encontrados")
            
            with st.expander(f"📋 Ver IDs ({len(record_ids)} elementos)"):
                st.write(record_ids)
            
            return record_ids
            
        except Exception as e:
            st.error(f"❌ Error al procesar CSV: {e}")
            return None
    
    return None

# =========================================
# Verificación del Sistema
# =========================================
def check_system_requirements():
    st.subheader("🔍 Verificación de Requisitos")
    
    checks = []
    
    try:
        chrome_options = Options()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=chrome_options)
        driver.quit()
        checks.append(("✅", "Chrome", "Disponible"))
    except Exception as e:
        checks.append(("❌", "Chrome", f"No disponible: {str(e)[:50]}..."))
    
    for status, component, message in checks:
        st.write(f"{status} **{component}**: {message}")
    
    return all(check[0] == "✅" for check in checks)

# =========================================
# Interfaz Principal
# =========================================
st.markdown("""
<div class='header-container'>
    <h1>🧬 Extracción de Códigos de Barras</h1>
    <p class='header-subtitle'>Lab Muestras Humanas • Proyecto PRESIENTE</p>
</div>
""", unsafe_allow_html=True)
st.markdown(obtener_estilos_css(), unsafe_allow_html=True)

with st.expander("🔧 Verificación del Sistema"):
    if st.button("Ejecutar Verificación"):
        system_ok = check_system_requirements()
        if not system_ok:
            st.warning("⚠️ Algunos requisitos faltan")

st.subheader("🎯 Elegir Método de Entrada")
input_method = st.radio(
    "¿Cómo proporcionar Record IDs?",
    ["Entrada Manual", "Carga de CSV"],
    horizontal=True
)

record_ids = []

if input_method == "Entrada Manual":
    st.subheader("✍️ Entrada Manual")
    record_ids_input = st.text_input(
        "Ingresa Record IDs separados por comas", 
        placeholder="ej., 1,2,3,4,5",
        value="1,2,3"
    )
    
    if record_ids_input.strip():
        try:
            for rid in record_ids_input.split(","):
                rid = rid.strip()
                if rid:
                    try:
                        record_ids.append(int(rid))
                    except ValueError:
                        st.warning(f"⚠️ '{rid}' no es válido")
        except Exception as e:
            st.error(f"❌ Error: {e}")

elif input_method == "Carga de CSV":
    csv_record_ids = process_csv_upload()
    if csv_record_ids:
        record_ids = csv_record_ids

if record_ids:
    st.subheader("📧 Configuración de Email")
    st.success(f"✅ Listo para procesar {len(record_ids)} Record IDs")
    
    email_receiver_input = st.text_input(
        "Email del Destinatario",
        placeholder="ejemplo@dominio.com"
    )
    
    if st.button("🚀 Descargar y Enviar Email", type="primary"):
        if not email_receiver_input.strip():
            st.error("❌ Ingresa un email válido")
        else:
            try:
                st.info(f"🎯 Procesando {len(record_ids)} Record IDs...")
                
                with st.spinner("📥 Descargando..."):
                    downloaded_files = download_barcode_images(record_ids, redcap_username, redcap_password)

                if downloaded_files:
                    st.success(f"✅ {len(downloaded_files)} muestras descargadas")

                    st.subheader("📸 Imágenes:")
                    cols = st.columns(min(3, len(downloaded_files)))
                    for i, file_path in enumerate(downloaded_files):
                        col_idx = i % len(cols)
                        with cols[col_idx]:
                            if os.path.exists(file_path):
                                record_id = os.path.basename(file_path).split('_')[-1].split('.')[0]
                                st.image(file_path, caption=f"Record {record_id}")

                    with st.spinner("📧 Enviando..."):
                        if send_email_with_zip(record_ids, downloaded_files, email_receiver_input):
                            st.success("✅ Email enviado exitosamente")
                            
                            zip_files = [f for f in os.listdir("codigos_barras") if f.endswith('.zip')]
                            if zip_files:
                                zip_file = zip_files[0]
                                zip_path = os.path.join("codigos_barras", zip_file)
                                if os.path.exists(zip_path):
                                    zip_size = os.path.getsize(zip_path) / (1024 * 1024)
                                    st.info(f"📦 {zip_file} ({zip_size:.2f} MB)")
                            
                            try:
                                shutil.rmtree("codigos_barras")
                                st.info("🧹 Archivos temporales limpiados")
                            except:
                                pass
                        else:
                            st.error("❌ Fallo al enviar")
                else:
                    st.error("❌ No se descargaron imágenes")

            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.exception(e)
