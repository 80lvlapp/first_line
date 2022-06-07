package models

import (
	u "first-line/utils"
	"fmt"
	"github.com/jinzhu/gorm"
	"time"
)

type Tournament struct {
	gorm.Model
	Name               string           `json:"name" gorm:"not null"`
	Date               time.Time        `json:"date" gorm:"not null"`
	Venue              string           `json:"venue" gorm:"not null"`
	IDTypeOfTournament uint             `json:"id_type_of_tournament" gorm:"not null"`
	TypeOfTournament   TypeOfTournament `json:"type_of_tournament" gorm:"foreignkey:IDTypeOfTournament"`
}

func (item *Tournament) Validate() (map[string]interface{}, bool) {
	if item.Name == "" {
		return u.Message(false, "Coach name should be on the payload"), false
	}

	return u.Message(true, "success"), true
}

func (item *Tournament) CreateTournament() map[string]interface{} {
	resp, ok := item.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(item)
	resp["tournament"] = item
	return resp
}

func UpdateTournament(id string, newItem Tournament) *Tournament {
	item := &Tournament{}
	err := GetDB().Table("tournaments").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Name = newItem.Name
	item.Date = newItem.Date
	item.Venue = newItem.Venue
	item.IDTypeOfTournament = newItem.IDTypeOfTournament
	GetDB().Save(item)
	return item

}

func GetTournament(id string) *Tournament {
	item := &Tournament{}
	err := GetDB().Table("tournaments").Preload("TypeOfTournament").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func DeleteTournament(id string) map[string]interface{} {

	db.Delete(&Tournament{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetTournaments() []*Tournament {
	items := make([]*Tournament, 0)
	err := GetDB().Table("tournaments").Preload("TypeOfTournament").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}
