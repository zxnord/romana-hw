# Serial-to-USB Converter Daemon

Este software permite la **conversión de puertos serial a USB** en sistemas Linux.  
Además, se encarga de mantener un **proceso vivo** en el arranque del sistema mediante `/etc/init.d/rc.local` y cuenta con un **cronjob semanal** que limpia los logs para evitar acumulación innecesaria de archivos.

---

## 📦 Requisitos

- Linux (Debian/Ubuntu/CentOS o derivados).
- Acceso root o permisos `sudo`.
- Paquetes:
  - `cron`
  - `screen` o `tmux` (opcional, para monitoreo interactivo).

---

## ⚙️ Instalación

1. **Descargar la imagen ISO**:

   ```bash
   wget https://drive.google.com/file/d/1zBoGT7Ne80816eYg430MmiAu9MGh7GbU/view?usp=sharing
   ```

2. **Copiar a memoria micro SD**:

   ```bash
   xzcat romana-luchetti-bkp.img.xz | dd of=/ruta/a/microSD status=progress bs=4M
   ```

## 🚀 Configuración de arranque (rc.local):

1. **Editar ```/etc/rc.local``` (antes de ```exit 0```)**:

   ```bash
   /home/ubuntu/romana-hw/src/script.sh &
   ```

2. **Guardar cambios y asegurarse que ```rc.local``` sea ejecutable**:

   ```bash
   sudo chmod 755 /etc/rc.local
   chmod 755 /home/ubuntu/romana-hw/src/script.sh
   chmod 755 /home/ubuntu/romana-hw/src/cleanup.sh
   ```

3. **Verificar que el proceso se carga en cada reinicio**:

   ```bash
   ps -fea | grep -i ros
   ```

## 🧹 Limpieza automática de logs

El sistema incluye un *cronjob cada 3 dias* para borrar logs viejos y mantener el sistema ligero.

1. **Editar el cronjob**:

   ```bash
   sudo crontab -e
   ```

2. **Agregar la siguiente línea (ejecuta cada 3 dias a las 0 AM)**:

   ```cron
   0 0 */3 * * /home/ubuntu/romana-hw/cleanup.sh
   ```

## 🔍 Logs

Los logs se guardan en:

   ```bash
   /var/log
   ```
   - romana_serial.log  →  Actividad principal del servicio.
   - romana_serial_error.log  →  Errores y advertencias.

## 🛠️ Mantenimiento

- Verificar que el cronjob siga activo

   ```bash
   sudo crontab -l
   ```
- Si el servicio no inicia al reiniciar:

   - Revisar permisos de `/etc/rc.local`.
   - Verificar rutas absolutas.