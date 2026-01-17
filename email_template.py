"""Template de email profesional corporativo."""

from datetime import datetime
import os


def generar_email_html(total_capturas, total_records, zip_filename, zip_size_mb):
    """
    Genera el HTML del email profesional.
    
    Args:
        total_capturas (int): Número total de capturas
        total_records (int): Número total de Record IDs
        zip_filename (str): Nombre del archivo ZIP
        zip_size_mb (float): Tamaño del ZIP en MB
        
    Returns:
        str: HTML del email
    """
    fecha_generacion = datetime.now().strftime("%d/%m/%Y %H:%M")
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    </head>
    <body style="margin: 0; padding: 0; background: linear-gradient(135deg, #2d3e1f 0%, #3d5228 100%); font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;">
        
        <!-- Contenedor principal con degradado oscuro -->
        <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background: linear-gradient(135deg, #2d3e1f 0%, #3d5228 100%); padding: 40px 20px;">
            <tr>
                <td align="center">
                    
                    <!-- Card principal - Fondo beige/crema -->
                    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="700" style="max-width: 700px; width: 100%; background: #f5f3ed; border-radius: 16px; overflow: hidden; box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);">
                        
                        <!-- Header corporativo -->
                        <tr>
                            <td style="background: linear-gradient(135deg, #556620 0%, #3d4a18 100%); padding: 48px 32px; text-align: center; position: relative;">
                                <h1 style="margin: 0; color: #D4E157; font-size: 32px; font-weight: 800; letter-spacing: -1px; text-shadow: 0 2px 4px rgba(0,0,0,0.2);">🧬 Códigos de Barras Generados</h1>
                                <p style="margin: 10px 0 0 0; color: rgba(255, 255, 255, 0.9); font-size: 15px; font-weight: 500; letter-spacing: 0.5px;">Lab Muestras Humanas • Proyecto PRESIENTE</p>
                                <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 4px; background: linear-gradient(90deg, #D4E157 0%, #C8E100 50%, #D4E157 100%);"></div>
                            </td>
                        </tr>
                        
                        <!-- Content -->
                        <tr>
                            <td style="padding: 40px 32px;">
                                
                                <!-- Stats HORIZONTALES -->
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="margin-bottom: 32px;">
                                    <tr>
                                        <!-- Stat 1 -->
                                        <td width="48%" style="padding-right: 12px;">
                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background: linear-gradient(135deg, #faf8f4 0%, #f2ede3 100%); border-left: 4px solid #C8E100; border-radius: 12px; padding: 28px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                                                <tr>
                                                    <td align="center">
                                                        <div style="font-size: 48px; font-weight: 800; color: #3d4a18; margin-bottom: 6px; line-height: 1;">{total_capturas}</div>
                                                        <div style="font-size: 11px; color: #5a6c3e; text-transform: uppercase; letter-spacing: 1.2px; font-weight: 700;">Muestras Capturadas</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                        
                                        <!-- Stat 2 -->
                                        <td width="48%" style="padding-left: 12px;">
                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background: linear-gradient(135deg, #faf8f4 0%, #f2ede3 100%); border-left: 4px solid #C8E100; border-radius: 12px; padding: 28px 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.06);">
                                                <tr>
                                                    <td align="center">
                                                        <div style="font-size: 48px; font-weight: 800; color: #3d4a18; margin-bottom: 6px; line-height: 1;">{total_records}</div>
                                                        <div style="font-size: 11px; color: #5a6c3e; text-transform: uppercase; letter-spacing: 1.2px; font-weight: 700;">Record IDs</div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                
                                <!-- Info Card -->
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background: #faf8f4; border: 2px solid #e8e4da; border-radius: 12px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                                    <tr>
                                        <td style="padding: 28px 24px;">
                                            <h2 style="margin: 0 0 18px 0; color: #3d4a18; font-size: 15px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px;">📦 Detalles del Archivo</h2>
                                            
                                            <!-- Info Rows -->
                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                                <tr style="border-bottom: 2px solid #f0ece2;">
                                                    <td style="color: #5a6c3e; font-size: 14px; padding: 14px 0; font-weight: 600;">Archivo</td>
                                                    <td align="right" style="color: #2d3e1f; font-size: 14px; padding: 14px 0; font-weight: 700;">{zip_filename}</td>
                                                </tr>
                                                <tr style="border-bottom: 2px solid #f0ece2;">
                                                    <td style="color: #5a6c3e; font-size: 14px; padding: 14px 0; font-weight: 600;">Tamaño</td>
                                                    <td align="right" style="color: #556620; font-size: 16px; padding: 14px 0; font-weight: 800;">{zip_size_mb:.2f} MB</td>
                                                </tr>
                                                <tr>
                                                    <td style="color: #5a6c3e; font-size: 14px; padding: 14px 0; font-weight: 600;">Fecha de Generación</td>
                                                    <td align="right" style="color: #2d3e1f; font-size: 14px; padding: 14px 0; font-weight: 700;">{fecha_generacion}</td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                
                                <!-- Nomenclatura -->
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background: #faf8f4; border-left: 4px solid #C8E100; border-radius: 10px; margin-bottom: 24px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
                                    <tr>
                                        <td style="padding: 24px 24px;">
                                            <h3 style="margin: 0 0 16px 0; color: #3d4a18; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.8px;">📋 Nomenclatura de Archivos</h3>
                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                                <tr>
                                                    <td style="color: #4a5a32; font-size: 13px; padding: 8px 0; line-height: 1.6;">
                                                        <code style="background: linear-gradient(135deg, #f0ece2 0%, #e8e4da 100%); color: #3d4a18; padding: 6px 12px; border-radius: 6px; font-family: 'SF Mono', 'Monaco', 'Courier New', monospace; font-size: 12px; font-weight: 700; border: 1px solid #d4d0c6;">Muestra_record_{{ID}}.png</code>
                                                        <span style="margin-left: 12px; color: #5a6c3e; font-weight: 600;">→ Muestra del Record ID correspondiente</span>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                                
                                <!-- Alert -->
                                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background: linear-gradient(135deg, #fffbf0 0%, #fff8e1 100%); border: 2px solid #ffca28; border-left: 5px solid #f57f17; border-radius: 10px; box-shadow: 0 2px 8px rgba(245,127,23,0.1);">
                                    <tr>
                                        <td style="padding: 20px 24px;">
                                            <p style="margin: 0; color: #2d3e1f; font-size: 13px; line-height: 1.7; font-weight: 500;">
                                                <strong style="color: #e65100; font-weight: 800; font-size: 14px;">💡 Instrucciones:</strong><br>
                                                Descarga y descomprime el archivo ZIP adjunto para acceder a las imágenes de los códigos de barras de las muestras.
                                            </p>
                                        </td>
                                    </tr>
                                </table>
                                
                            </td>
                        </tr>
                        
                        <!-- Footer corporativo -->
                        <tr>
                            <td style="background: linear-gradient(135deg, #3d4a18 0%, #2d3e1f 100%); padding: 32px 24px; text-align: center; border-top: 3px solid #C8E100;">
                                <div style="display: inline-block; background: linear-gradient(135deg, #D4E157 0%, #C8E100 100%); color: #1a2510; padding: 10px 24px; border-radius: 20px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 16px; box-shadow: 0 4px 12px rgba(212,225,87,0.3);">⚡ AUTOMATIZADO</div>
                                <p style="margin: 8px 0 4px 0; color: rgba(255, 255, 255, 0.7); font-size: 12px; font-weight: 500; letter-spacing: 0.3px;">Sistema de Extracción de Códigos de Barras</p>
                                <p style="margin: 4px 0; color: #D4E157; font-size: 15px; font-weight: 700; letter-spacing: 0.5px;">OuraByte • Proyecto PRESIENTE</p>
                                <p style="margin: 8px 0 0 0; color: rgba(255, 255, 255, 0.4); font-size: 11px; font-weight: 500;">&copy; {datetime.now().year} • Todos los derechos reservados</p>
                            </td>
                        </tr>
                        
                    </table>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
