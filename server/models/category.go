package models

import (
	u "first-line/utils"
	"fmt"
	"github.com/jinzhu/gorm"
)

type Category struct {
	gorm.Model
	Name            string          `json:"name" gorm:"not null"`
	ValueCategories []ValueCategory `json:"value_categories" gorm:"foreignkey:CategoryId"`
}

func (category *Category) Validate() (map[string]interface{}, bool) {

	if category.Name == "" {
		return u.Message(false, "Contact name should be on the payload"), false
	}
	return u.Message(true, "success"), true
}

func (item *Category) CreateCategory() map[string]interface{} {

	//if resp, ok := category.Validate(); !ok {
	//	return resp
	//}

	GetDB().Create(item)

	resp := u.Message(true, "success")
	resp["category"] = item
	return resp
}

func GetCategory(id string) *Category {
	item := &Category{}
	err := GetDB().Table("categories").Preload("ValueCategories").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func GetCategorys() []*Category {
	items := make([]*Category, 0)
	err := GetDB().Table("categories").Preload("ValueCategories").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}

func UpdateCategory(id string, newSchool Category) *Category {
	item := &Category{}
	err := GetDB().Table("categories").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Name = newSchool.Name
	GetDB().Save(item)
	return item

}

func DeleteCategory(id string) map[string]interface{} {

	db.Delete(&Category{}, id)
	resp := u.Message(true, "success")
	return resp

}
