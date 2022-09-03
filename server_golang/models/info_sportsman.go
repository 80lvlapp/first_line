package models

import (
	school "first-line/school"
	u "first-line/utils"
	"fmt"
	"time"
)

type InfoSportsman struct {
	Period        time.Time     `json:"orderedAt" gorm:"not null;"`
	IDSportsman   uint          `json:"id_sportsman" gorm:"not null;"`
	IDCoach       uint          `json:"id_coach" gorm:"not null;"`
	IDSportSchool uint          `json:"id_sport_school" gorm:"not null;"`
	Insurance     bool          `json:"insurance" gorm:"default: false;not null"`
	Sportsman     Sportsman     `json:"sportsman" gorm:"foreignkey:IDSportsman"`
	Coach         Coach         `json:"coach" gorm:"foreignkey:IDCoach"`
	School        school.School `json:"school" gorm:"foreignkey:IDSportSchool"`
}

func (item *InfoSportsman) Validate() (map[string]interface{}, bool) {
	//if item.Name == "" {
	//	return u.Message(false, "Coach name should be on the payload"), false
	//}

	return u.Message(true, "success"), true
}

func (item *InfoSportsman) CreateInfoSportsman() map[string]interface{} {
	resp, ok := item.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(item)
	resp["info_sportsman"] = item
	return resp
}

func UpdateInfoSportsman(id string, newItem InfoSportsman) *InfoSportsman {
	item := &InfoSportsman{}
	err := GetDB().Table("info_sportsmen").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Period = newItem.Period
	item.IDSportsman = newItem.IDSportsman
	item.IDCoach = newItem.IDCoach
	item.IDSportSchool = newItem.IDSportSchool
	item.Insurance = newItem.Insurance

	GetDB().Save(item)
	return item

}

func GetInfoSportsman(id string) *InfoSportsman {
	item := &InfoSportsman{}
	err := GetDB().Table("info_sportsmen").Preload("School").Preload("Coach").Preload("Sportsman").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func DeleteInfoSportsman(id string) map[string]interface{} {

	db.Delete(&InfoSportsman{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetInfoSportsmen() []*InfoSportsman {
	items := make([]*InfoSportsman, 0)
	dataBase := GetDB()
	//err := GetDB().Table("info_sportsmen").Preload("School").Find(&items).Error
	err := dataBase.Table("info_sportsmen").Preload("School").Preload("Coach").Preload("Sportsman").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}
