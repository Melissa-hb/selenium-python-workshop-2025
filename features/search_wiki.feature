Feature: Busqueda de tema
  Scenario: Busqueda correcta
    Given el usuario se encuentra en la pagina principal de wikipedia
    When el usuario escribe el tema Python (lenguaje de programación) en el buscador
    Then aparece el titulo Python