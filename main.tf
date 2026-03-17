provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "demo" {
  name     = "streamlit-demo-rg"
  location = "Southeast Asia"
}

# App Service Plan (Linux)
resource "azurerm_service_plan" "demo" {
  name                = "streamlit-demo-plan"
  location            = azurerm_resource_group.demo.location
  resource_group_name = azurerm_resource_group.demo.name
  os_type             = "Linux"
  sku_name            = "B1"
}

# Web App (Docker Container)
resource "azurerm_linux_web_app" "streamlit" {
  name                = "streamlit-demo-${random_string.suffix.result}"
  location            = azurerm_resource_group.demo.location
  resource_group_name = azurerm_resource_group.demo.name
  service_plan_id     = azurerm_service_plan.demo.id

  site_config {
    application_stack {
      docker_image_name = "jane0123/streamlit-demo:v2"
    }
  }

  app_settings = {
    WEBSITES_PORT = "8000"
  }
}

# Random suffix (to avoid name conflict)
resource "random_string" "suffix" {
  length  = 5
  special = false
  upper   = false
}