# Pydantic

## Web page

web page [https://docs.pydantic.dev/latest/]

## Serialización

codigo: serializacion.py

Ejemplo sobre como serializar a formato Dic o Json desde el formato interno de pydantic (Pydantic class)

Los archivos json_ejemplo y dict_ejemplo contienen datos tipo dict y json que se usan en el ejemplo para validar.

## Deserialización

codigo: deserializacion.py

Ejemplo sobre como deserializar desde formato Dic o Json hacia el formato interno de pydantic (Pydantic class)

Los archivos json_ejemplo y dict_ejemplo contienen datos tipo dict y json que se usan en el ejemplo para validar.

## Generación de Modelo

codigo: model_generation.py

A partir de las clases, se generan los archivos .json y .yaml, que pueden usarse como modelo de datos en un CU.

## Validación

codigo: validacion.py

Realiza la validación de un modelo de datos modelo.yaml.

## Coercion

codigo: coercion.py

Ejemplo que muestra como los tipos de datos se ajustan segun el modo coercion sea estricto o no.
