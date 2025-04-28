Feature: Busqueda del producto 
  Scenario: Busqueda correcta
    Given el usuario se encuentra en la pagina principal de mercado libre
    When el usuario escribe el producto iPhone 13
    Then aparecen productos contienen el nombre iPhone