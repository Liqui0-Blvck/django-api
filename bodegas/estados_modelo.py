### estados modelos App Bodegas###

CALIBRES = (
    ('Categoria 1', (
        ('0','Sin Calibre'),
        ('1', 'PreCalibre'),
        ('2','18/20'),
        ('3','20/22'),
        ('4','23/25'),
        ('5','25/27'),
        ('6','27/30'),
        ('7','30/32'),
        ('8','32/34'),
        ('9','34/36'),
        ('10','36/40'),
        ('11','40+'), 
    )),
    ('Elaborados', (
        ('12', '3x5mm'),
        ('13', '2x4mm'),
        ('14', '4x6mm'),
        ('15', '3x5mm'),
        ('16', '2x4mm'),
        ('17', '4x6mm'),
        ('18', '+2mm'),
        ('19', '-2mm'),
        ('20', '+2mm'),  
        ('21', '-2mm'), 
    ))
)

VARIEDAD = (    
('SL','Solano'),
('MO','Mono'),
('CM','Carmel'),
('RB','Ruby'),
('PR','Price'),
('WC','Wood Colony'),
('TK','Tokio'),
('MD','Merced'),
('TC','Tuca'),
('NP','Nonpareil'),
('RV','Revueltas'),
('PD','Padre'),
('TX','Texas'),
('MC','Marcona'),
('GU','Guara'),
('DS','Desmayo'),
('IX','Ixl'),
('TH','Thompson'),
('DK','Drake'),
('VS','Vesta'),
('NL','Neplus'),
('FR','Fritz'),
('BU','Butte'),
('MI','Mission'),
('NE','Neplus'),
('CA','Tipo California'),
('MZ','Mezcla'),
('ID','Independence'),
('AV','Avijar'),
('IS','Isabelona'),
('ST','Soleta'),
('VI','Vialfas'),
)

CALIDAD = (
    ('Categoria 1', (
        ('EXT', 'Extra N°1'), ### EXT
        ('SUP', 'Supreme'), ### SUP
        ('W&B', 'Whole & Broken'), ### W&B
    )),
    ('Elaborados', (
        ('har_cn_piel', 'Harina Con Piel'),
        ('har_sn_piel', 'Harina Sin Piel'),
        ('gra_cn_piel', 'Granillo Con Piel'),
        ('gra_sn_piel', 'Granillo Sin Piel'),
        ('gra_tos_s_pl', 'Granillo Tostado Sin Piel'),
        ('gra_tos_c_pl', 'Granillo Tostado Con Piel'),
        ('alm_tostada', 'Almendras Tostadas'),
        ('alm_repelada', 'Almendras Repeladas'),
    )),
    ('Categoria 2', (
        ('vana', 'Vana'),
        ('goma', 'Goma'),
        ('insect', 'Insecto'),
        ('hongo', 'Hongo'),
        ('des_sea', 'Descarte Sea'),
        ('polvillo', 'Polvillo'),
        ('pepasuelo', 'Pepa Suelo'),
        ('preca', 'Precalibre'),
    )),
)

NOMBRE_PRODUCTO = (
    ('1', 'Almendras'),
    ('2', 'Granillo'),
    ('3', 'Harina'),
)

PRODUCTO = (
    ('pepa_expo', 'Pepa Exportacion'),
    ('whole', 'Whole & Broken'),
    ('picada', 'Picada'),
    ('trozo', 'Trozo'),    
    ('pepa_huerto', 'Pepa Huerto'),
    ('dano_insecto', 'Daño Insecto'),
    ('descarte_sea', 'Descarte Sea'),
    ('fruta_suelo', 'Fruta Suelo'),
    ('goma', 'Goma'),
    ('hongos', 'Hongos'),
    ('polvillo', 'Polvillo Almendra'),
    ('basura', 'Basura'),
    ('recalibre', 'Recalibre'),

)

ESTADO_BIND_EN_FIGORIFICO = (
    ('en_bodega', 'Bin Materia Prima Disponible'),
    ('en_programa', 'Bin asignado a Programa'),
    ('procesado','Bin Procesado'),
    ('5', 'Agrupado')
)

ESTADO_BIN_EN_BODEGAG6 = (
    ('bin_procesado', 'Bin procesado en Proceso'),
    ('en_espera', 'Bin esperando validacion'),
    ('bin_asignado_proceso', 'Bin asignado a Proceso'),
)

CALLE_BODEGA_1 = (
    ('-', 'Seleccione Calle'),
    ('F', 'Calle de Fumigado'),
    ('1', 'Calle 1'),
    ('2', 'Calle 2'),
    ('3', 'Calle 3'),
    ('4', 'Calle 4'),
    ('5', 'Calle 5'),
)

CALLE_BODEGA_2 = (
    ('-', 'Seleccione Calle'),
    ('F', 'Calle de Fumigado'),
    ('1', 'Calle 1'),
    ('2', 'Calle 2'),
    ('3', 'Calle 3'),
    ('4', 'Calle 4'),
    ('5', 'Calle 5'),
    ('6', 'Calle 6'),
    ('7', 'Calle 7'),
    ('8', 'Calle 8'),
    ('9', 'Calle 9'),
    ('10', 'Calle 10'),
    ('11', 'Calle 11'),
    ('12', 'Calle 12'),
)

CALLE_BODEGA_3 = (
    ('-', 'Seleccione Calle'),
    ('F', 'Calle de Fumigado'),
    ('1', 'Calle 1'),
    ('2', 'Calle 2'),
    ('3', 'Calle 3'),
    ('4', 'Calle 4'),
    ('5', 'Calle 5'),
    ('6', 'Calle 6'),
    ('7', 'Calle 7'),
    ('8', 'Calle 8'),
    ('9', 'Calle 9'),
    ('10', 'Calle 10'),
    ('11', 'Calle 11'),
    ('12', 'Calle 12'),
    ('13', 'Calle 13'),
    ('14', 'Calle 14'),
    ('15', 'Calle 15'),
    ('16', 'Calle 16'),
    ('17', 'Calle 17'),
    ('18', 'Calle 18'),
    ('19', 'Calle 19'),
    ('20', 'Calle 20'),
    ('21', 'Calle 21'),
    ('22', 'Calle 22'),
    ('23', 'Calle 23'),
    ('24', 'Calle 24'),
    ('25', 'Calle 25'),

)

CALLE_BODEGA_4 = (
    ('-', 'Seleccione Calle'),
    ('F', 'Calle de Fumigado'),
    ('1', 'Calle 1'),
    ('2', 'Calle 2'),
    ('3', 'Calle 3'),
    ('4', 'Calle 4'),
    ('5', 'Calle 5'),
    ('6', 'Calle 6'),
    ('7', 'Calle 7'),
    ('8', 'Calle 8'),
    ('9', 'Calle 9'),
    ('10', 'Calle 10'),
    ('11', 'Calle 11'),
    ('12', 'Calle 12'),
    ('13', 'Calle 13'),
    ('14', 'Calle 14'),
    ('15', 'Calle 15'),
    ('16', 'Calle 16'),
    ('17', 'Calle 17'),
    ('18', 'Calle 18'),
    ('19', 'Calle 19'),
    ('20', 'Calle 20'),
    ('21', 'Calle 21'),
    ('22', 'Calle 22'),
    ('23', 'Calle 23'),
    ('24', 'Calle 24'),
    ('25', 'Calle 25'),
  
)




CALLE_BODEGA_G5 = (
    ('-', 'Seleccione Calle'),
    ('F', 'Calle de Fumigado'),
    ('1', 'Calle 1'),
    ('2', 'Calle 2'),
    ('3', 'Calle 3'),
    ('4', 'Calle 4'),
    ('5', 'Calle 5'),
    ('6', 'Calle 6'),
    ('7', 'Calle 7'),
    ('8', 'Calle 8'),
    ('9', 'Calle 9'),
    ('10', 'Calle 10'),
    ('11', 'Calle 11'),
    ('12', 'Calle 12'),
    ('13', 'Calle 13'),
    ('14', 'Calle 14'),
    ('15', 'Calle 15'),
    ('16', 'Calle 16'),
    ('17', 'Calle 17'),
    ('18', 'Calle 18'),
    ('19', 'Calle 19'),
    ('20', 'Calle 20'),
)


FILA = (
    ('-', 'En Programa'),
    ('A', 'Columna A'),
    ('B', 'Columna B'),
    ('C', 'Columna C'),
    ('D', 'Columna D'),
)

POSICION = (
    ('-', 'En Programa'),
    ('1', 'Espacio 1'),
    ('2', 'Espacio 2'),
    ('3', 'Espacio 3'),
    ('4', 'Espacio 4'),
    ('5', 'Espacio 5'),
    ('6', 'Espacio 6'),
    ('7', 'Espacio 7'),
    ('8', 'Espacio 8'),
)

TIPOS_BIN = (
    (40, 'Patineta Negra'),
    (43.5, 'Patineta Blanca'),
    (44.6, 'UPC'),
 
)


UBICACION_PATIO_TECHADO_EXT = (
    ('0','Pendiente Ubicacion'),
    ('1','Sector 1'),
    ('2','Sector 2'),
    ('3','Sector 3'),
)

UBICACION_PATIO_TECHADO_EXT_LI = (
    ('0', 'Asigne Ubicación'),
    ('1','Sector 1'),
    ('2','Sector 2'),
    ('3','Sector 3'),
    ('4', 'Pavo'),
)


ESTADO_SEMI_ELAB_G6 = (
    ('creado', 'Producto Semi Elab. Disponible'),
    ('reing_programa', 'SemiElab Para Reingreso Programa'),
    ('en_proceso', 'Semi Elaborado en Proceso'),
    ('procesado', 'Convertida en Producto Elab G7'),
    ('en_embalaje','Bin Asignado a Embalaje'),
)

TIPOS_RESULTANTES_MATPRIMA = (
    ('precal_tostado', 'Precalibre Tostado'),
    ('almend_tosta_con_piel', 'Almendra Tostada con piel'),
    ('almend_tosta_sin_piel', 'Almendra Tostada sin piel'),
    ('no_indicado', 'No Indicado'),
)

TIPOINGRESO_PRODUC_ELAB_G7 = (
    ('exedente', 'Exedente resultante Proceso G6'),
    ('procesado', 'Ingreso Producto Elaborado G7'),
)
PROCESO = (
    ('Proceso de Granillado',(
        ('granillo_conpiel_3mm', 'Granillo con Piel 3mm'),
        ('granillo_conpiel_2mm', 'Granillo con Piel 2mm'),
        ('granillo_sinpiel_3mm', 'Granillo sin Piel 3mm'),
        ('granillo_sinpiel_2mm', 'Granillo sin Piel 2mm'),
    )),
    ('Proceso de Harina',(
        ('harina_con_piel', 'Harina Con Piel'),
        ('harina_sin_piel', 'Harina Sin Piel'),
    )), 
)


ESTADO_SEMI_ELAB_G7 = (
    ('creado', 'Producto Semi Elab. Disponible'),
    ('reing_programa', 'SemiElab Para Reingreso Programa'),
    ('en_proceso', 'Semi Elaborado en Proceso'),
    ('procesado', 'Convertida en Producto Elab G7'),
    ('en_embalaje','Bin Asignado a Embalaje'),
)



ESTADO_CODIGO_BIN = (
    ('espe_validacion','Esperando Validacion Inventario'),
    ('validado_en_inve','Validado en Inventario'),
    
)


ESTADO_BIN_G1 = (
    ('0', 'En Reproceso'),
    ('1','En Bodega'),
    ('2','En Programa'),
    ('3','Procesado'),
    ('4', 'Transferido a G5'),
    ('5', 'Agrupado')
)

ESTADO_BIN_G2 = (
    ('0', 'En Reproceso'),
    ('1','En Bodega'),
    ('2','En Programa'),
    ('3','Procesado'),
    ('4', 'Transferido a G5'),
    ('5', 'Agrupado')
)
ESTADO_BIN_G3_G4 = (
    ('0', 'En Reproceso'),
    ('1','En Bodega'),
    ('2','En Programa'),
    ('3','Procesado'),
    ('4', 'Transferido a G5'),
    ('5', 'Agrupado')
)

ESTADO_PROGRAMA_SELECCION = (
    ('0', 'En Construcción del Programa'),
    ('1','En espera de Inicio'),
    ('2','En Ejecución'),
    ('3','Pausado'),
    ('4','Programa Terminado'),
    ('5','Programa Cerrado'),
    ('6','Fin pausa Programa'),
    ('A','Inicio del Re-Proceso'),
    ('B','Fin del Re-Proceso'),
    
)

ESTADO_GUIA_PATIO_EXT = (
   
    ('1','Creada'),
    ('2','Asignando Ubicaciones'),
    ('3','Ubicacion Asignada'),
)

ESTADO_ENVASE_EN_PATIO_EXT = (
    ('0', 'En Reproceso'),
    ('1', 'En Patio techado'),
    ('2', 'En Produccion'),
    ('3', 'Procesado'),
)

ESTADO_GUIA_INGRESO_BODEGA = (
    ('0', 'Registrado'),
    ('1','En espera'),
    ('2','Sector Asignado'),
    ('3','Descargado'),
)

ESTADO_TARJA_TRANSFERIDA = (
    ('0', 'Transferida a Bodega G5'),
    ('1', 'En Programa Planta Harina'),
    ('2', 'En Proceso Planta Harina'),
    ('3', 'Procesada en Planta Harina'),
    ('4', 'Tarja Devuelta a G4'),
)

ESTADOS_TRANSFERENCIAS = (
    ('0', 'Creada'), 
    ('1', 'Completada'),
    ('2', 'Anulada'),  
)


ESTADOS_FUMIGACION = (
    ('0', 'Agregue bins para Fumigacion'),
    ('1', 'Fumigacion Iniciada'),
    ('2', 'Fumigacion Terminada'),
)

BODEGAS_PRODALMEN = (
    ('G1', 'Bodega G1'),
    ('G2', 'Bodega G2'),
    ('G3', 'Bodega G3'),
    ('G4', 'Bodega G4'),
    ('G5', 'Bodega G5'),
    ('G6', 'Bodega G6'),
    ('G7', 'Bodega G7'),
)