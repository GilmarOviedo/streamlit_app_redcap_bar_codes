"""Estilos CSS profesionales para la aplicación."""

def obtener_estilos_css():
    """Retorna los estilos CSS de la aplicación."""
    return """
    <style>
    /* ============================================
       ESTILOS GLOBALES Y FUENTES
       ============================================ */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
    
    * {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }
    
    /* ============================================
       CONTENEDOR PRINCIPAL
       ============================================ */
    .main {
        background: linear-gradient(135deg, #f8f9f7 0%, #e8ebe5 100%);
        padding: 2rem 1rem;
    }
    
    /* ============================================
       HEADER PRINCIPAL
       ============================================ */
    .header-container {
        background: linear-gradient(135deg, #556620 0%, #3d4a18 100%);
        padding: 2.5rem 2rem;
        border-radius: 16px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
        border: 3px solid #C8E100;
    }
    
    .header-container h1 {
        color: #D4E157;
        font-size: 28px;
        font-weight: 800;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    .header-subtitle {
        color: rgba(255, 255, 255, 0.9);
        font-size: 14px;
        font-weight: 500;
        margin: 0;
        letter-spacing: 0.3px;
    }
    
    /* ============================================
       SECCIONES
       ============================================ */
    .section-header {
        background: linear-gradient(135deg, #3d4a18 0%, #556620 100%);
        color: #D4E157;
        padding: 1rem 1.5rem;
        border-radius: 10px;
        font-size: 16px;
        font-weight: 700;
        margin: 1.5rem 0 1rem 0;
        border-left: 5px solid #C8E100;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* ============================================
       CARDS Y CONTENEDORES
       ============================================ */
    .info-card {
        background: linear-gradient(135deg, #e8f5cd 0%, #d4e89e 100%);
        border: 2px solid #9ccc65;
        border-left: 4px solid #689f38;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(104, 159, 56, 0.1);
    }
    
    .success-card {
        background: linear-gradient(135deg, #c5e1a5 0%, #aed581 100%);
        border: 2px solid #689f38;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    .warning-card {
        background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
        border: 2px solid #fdd835;
        border-left: 4px solid #f57f17;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem 0;
    }
    
    /* ============================================
       BOTONES
       ============================================ */
    .stButton > button {
        background: linear-gradient(135deg, #556620 0%, #3d4a18 100%);
        color: #D4E157;
        border: 2px solid #C8E100;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 16px;
        font-weight: 700;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(85, 102, 32, 0.3);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #6a7f28 0%, #4d5a20 100%);
        border-color: #D4E157;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(85, 102, 32, 0.4);
    }
    
    /* ============================================
       INPUTS
       ============================================ */
    .stTextInput > div > div > input {
        border: 2px solid #e8ebe5;
        border-radius: 8px;
        padding: 0.75rem;
        font-size: 14px;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #C8E100;
        box-shadow: 0 0 0 3px rgba(200, 225, 0, 0.1);
    }
    
    /* ============================================
       RADIO BUTTONS
       ============================================ */
    .stRadio > div {
        background: linear-gradient(135deg, #e8f5cd 0%, #d4e89e 100%);
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #9ccc65;
    }
    
    /* ============================================
       EXPANDERS
       ============================================ */
    .streamlit-expanderHeader {
        background: linear-gradient(135deg, #c5e1a5 0%, #aed581 100%);
        border: 2px solid #689f38;
        border-radius: 8px;
        font-weight: 600;
        color: #1b5e20;
    }
    
    .streamlit-expanderContent {
        background: linear-gradient(135deg, #e8f5cd 0%, #d4e89e 100%);
        border: 2px solid #9ccc65;
        border-top: none;
        border-radius: 0 0 8px 8px;
    }
    
    /* ============================================
       DATAFRAMES
       ============================================ */
    .dataframe {
        background: linear-gradient(135deg, #e8f5cd 0%, #d4e89e 100%);
        border: 2px solid #9ccc65;
        border-radius: 8px;
        overflow: hidden;
    }
    
    .dataframe th {
        background: linear-gradient(135deg, #c5e1a5 0%, #aed581 100%) !important;
        color: #1b5e20 !important;
        font-weight: 700 !important;
    }
    
    .dataframe td {
        background: transparent !important;
        color: #2d3e1f !important;
    }
    
    /* ============================================
       PROGRESS BAR
       ============================================ */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #C8E100 0%, #D4E157 100%);
    }
    
    /* ============================================
       MENSAJES DE ESTADO
       ============================================ */
    .stSuccess {
        background: linear-gradient(135deg, #f0f7e8 0%, #e8f5e0 100%);
        border-left: 4px solid #C8E100;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stWarning {
        background: linear-gradient(135deg, #fffbf0 0%, #fff8e1 100%);
        border-left: 4px solid #ffca28;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stError {
        background: linear-gradient(135deg, #fff0f0 0%, #ffe8e8 100%);
        border-left: 4px solid #d32f2f;
        border-radius: 8px;
        padding: 1rem;
    }
    
    .stInfo {
        background: linear-gradient(135deg, #f0f4ff 0%, #e8f0ff 100%);
        border-left: 4px solid #1976d2;
        border-radius: 8px;
        padding: 1rem;
    }
    
    /* ============================================
       IMÁGENES
       ============================================ */
    img {
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        border: 2px solid #e8ebe5;
    }
    
    /* ============================================
       SPINNER
       ============================================ */
    .stSpinner > div {
        border-top-color: #C8E100 !important;
    }
    
    /* ============================================
       FILE UPLOADER
       ============================================ */
    .stFileUploader {
        background: linear-gradient(135deg, #e8f5cd 0%, #d4e89e 100%);
        border: 3px dashed #689f38;
        border-radius: 12px;
        padding: 2rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(104, 159, 56, 0.15);
    }
    
    .stFileUploader:hover {
        border-color: #33691e;
        background: linear-gradient(135deg, #dcedc8 0%, #c5e1a5 100%);
        box-shadow: 0 4px 12px rgba(104, 159, 56, 0.25);
    }
    
    .stFileUploader > div {
        background: transparent !important;
    }
    
    /* ============================================
       DOWNLOAD BUTTON
       ============================================ */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #c5e1a5 0%, #aed581 100%);
        color: #1b5e20;
        border: 2px solid #689f38;
        border-radius: 8px;
        font-weight: 600;
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #aed581 0%, #9ccc65 100%);
        border-color: #33691e;
    }
    </style>
    """
