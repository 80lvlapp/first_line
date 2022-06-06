package models

import (
	u "first-line/utils"
	"fmt"
	"github.com/jinzhu/gorm"
)

type TypeOfTournament struct {
	gorm.Model
	Name string `json:"name" gorm:"not null; size: 50"`
}

func (item *TypeOfTournament) Validate() (map[string]interface{}, bool) {
	if item.Name == "" {
		return u.Message(false, "Coach name should be on the payload"), false
	}

	return u.Message(true, "success"), true
}

func (item *TypeOfTournament) CreateTypeOfTournament() map[string]interface{} {
	resp, ok := item.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(item)
	resp["type_of_tournament"] = item
	return resp
}

func UpdateTypeOfTournament(id string, newItem TypeOfTournament) *TypeOfTournament {
	item := &TypeOfTournament{}
	err := GetDB().Table("type_of_tournaments").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Name = newItem.Name

	GetDB().Save(item)
	return item

}

func GetTypeOfTournament(id string) *TypeOfTournament {
	item := &TypeOfTournament{}
	err := GetDB().Table("type_of_tournaments").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func DeleteTypeOfTournament(id string) map[string]interface{} {

	db.Delete(&TypeOfTournament{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetTypeOfTournaments() []*TypeOfTournament {
	items := make([]*TypeOfTournament, 0)
	err := GetDB().Table("type_of_tournaments").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}
