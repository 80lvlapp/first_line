package models

import (
	"fmt"
	"github.com/jinzhu/gorm"
	u "go-contacts/utils"
)

type Category struct {
	gorm.Model
	Name           string          `json:"name"`
	ValuesCategory []ValueCategory `gorm:"polymorphic:Owner;"`
}

type ValueCategory struct {
	ID        int
	Name      string
	OwnerID   int
	OwnerType string
}

/*
 This struct function validate the required parameters sent through the http request body

returns message and true if the requirement is met
*/
func (category *Category) Validate() (map[string]interface{}, bool) {

	if category.Name == "" {
		return u.Message(false, "Contact name should be on the payload"), false
	}

	//All the required parameters are present
	return u.Message(true, "success"), true
}

func (category *Category) Create() map[string]interface{} {

	if resp, ok := category.Validate(); !ok {
		return resp
	}

	GetDB().Create(category)

	resp := u.Message(true, "success")
	resp["category"] = category
	return resp
}

func GetCategory(id uint) *Category {
	category := &Category{}
	err := GetDB().Table("categories").Where("id = ?", id).First(category).Error
	if err != nil {
		return nil
	}
	return category
}

func GetCategorys() []*Category {
	category := make([]*Category, 0)
	err := GetDB().Table("categories").Preload("ValuesCategory").Find(&category).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return category
}
