#!/bin/bash

# Variables
FECHA=$(date +%F)
ORIGEN="/var/log"
DESTINO="/backups/logs"
ARCHIVO="logs_backup_$FECHA.tar.gz"

# Crear el directorio destino si no existe
mkdir -p $DESTINO

# Comprimir los logs
tar -czf $DESTINO/$ARCHIVO $ORIGEN/*.log

# Verificar si se creó el archivo correctamente
if [ $? -eq 0 ]; then
    echo "Backup exitoso: $DESTINO/$ARCHIVO"
else
    echo "Error al realizar el backup"
fi
