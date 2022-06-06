package models

import (
	u "first-line/utils"
	"fmt"
	"github.com/jinzhu/gorm"
)

type ValueCategory struct {
	gorm.Model
	Name       string     `json:"name" gorm:"not null"`
	CategoryId uint       `json:"category_id" gorm:"not null"`
	Categories []Category `json:"category" gorm:"foreignkey:ID"`
}

func (category *ValueCategory) Validate() (map[string]interface{}, bool) {

	if category.Name == "" {
		return u.Message(false, "Contact name should be on the payload"), false
	}
	return u.Message(true, "success"), true
}

func (item *ValueCategory) CreateValueCategory() map[string]interface{} {
	GetDB().Create(item)

	resp := u.Message(true, "success")
	resp["category_value"] = item
	return resp
}

func GetValueCategory(id string) *ValueCategory {
	item := &ValueCategory{}
	err := GetDB().Table("value_categories").Preload("Categories").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func GetValueCategorys() []*ValueCategory {
	items := make([]*ValueCategory, 0)
	err := GetDB().Table("value_categories").Preload("Categories").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}

func UpdateValueCategory(id string, newItem ValueCategory) *ValueCategory {
	item := &ValueCategory{}
	err := GetDB().Table("value_categories").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Name = newItem.Name
	item.CategoryId = newItem.CategoryId
	GetDB().Save(item)
	return item

}

func DeleteValueCategory(id string) map[string]interface{} {

	db.Delete(&ValueCategory{}, id)
	resp := u.Message(true, "success")
	return resp

}
