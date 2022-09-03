package models

import (
	u "first-line/utils"
	"fmt"
	"time"

	"github.com/jinzhu/gorm"
)

type Sportsman struct {
	gorm.Model
	Name      string    `json:"name" gorm:"not null"`
	DateBirth time.Time `json: "date_birth"`
}

func (item *Sportsman) Validate() (map[string]interface{}, bool) {
	if item.Name == "" {
		return u.Message(false, "Coach name should be on the payload"), false
	}

	return u.Message(true, "success"), true
}

func (item *Sportsman) CreateSportsman() map[string]interface{} {
	resp, ok := item.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(item)
	resp["sportsman"] = item
	return resp
}

func UpdateSportsman(id string, newItem Sportsman) *Sportsman {
	item := &Sportsman{}
	err := GetDB().Table("sportsmen").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Name = newItem.Name
	item.DateBirth = newItem.DateBirth

	GetDB().Save(item)
	return item

}

func GetSportsman(id string) *Sportsman {
	item := &Sportsman{}
	err := GetDB().Table("sportsmen").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func DeleteSportsman(id string) map[string]interface{} {

	db.Delete(&Sportsman{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetSportsmen() []*Sportsman {
	items := make([]*Sportsman, 0)
	err := GetDB().Table("sportsmen").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}
