terraform {
  cloud {
    organization = "demo-org-name"

    workspaces {
      name = "my-demo-workspace"
    }
    token = "y6XjD4fzNwWZ4Q.atlasv1.in5zRCPkpVJYSe3rzfec3dKBtkLFk5JZFH1zznnOpYp4Cc5kNv7VfMQzh0t9EDAhtDI"
  }
}



provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "myResourceGroup"
  location = "West Europe"
}

resource "azurerm_resource_group" "rg2" {
  name     = "myResourceGroup2"
  location = "uksouth"
}