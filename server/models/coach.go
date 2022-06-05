package models

import (
	u "first-line/utils"
	"fmt"

	"github.com/jinzhu/gorm"
)

type Coach struct {
	gorm.Model
	Name string `json:"name" gorm:"not null"`
}

func (сoach *Coach) Validate() (map[string]interface{}, bool) {
	if сoach.Name == "" {
		return u.Message(false, "Coach name should be on the payload"), false
	}

	return u.Message(true, "success"), true
}

func (item *Coach) CreateCoach() map[string]interface{} {
	resp, ok := item.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(item)
	resp["сoach"] = item
	return resp
}

func UpdateCoach(id string, newItem Coach) *Coach {
	item := &Coach{}
	err := GetDB().Table("coaches").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Name = newItem.Name
	GetDB().Save(item)
	return item

}

func GetCoach(id string) *Coach {
	item := &Coach{}
	err := GetDB().Table("coaches").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func DeleteCoach(id string) map[string]interface{} {

	db.Delete(&Coach{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetСoaches() []*Coach {
	items := make([]*Coach, 0)
	err := GetDB().Table("coaches").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}
