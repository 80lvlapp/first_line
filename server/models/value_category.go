package models

import "github.com/jinzhu/gorm"

type ValueCategory struct {
	gorm.Model
	Name string `json:"name" gorm:"not null"`
	OwnerID   int
	OwnerType string
}