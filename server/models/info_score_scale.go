package models

import (
	u "first-line/utils"
	"fmt"
	"time"
)

type InfoScoreScale struct {
	Period           time.Time        `json:"period" gorm:"not null;"`
	IDSportSchool    uint             `json:"id_sport_school" gorm:"not null;"`
	IDTypeTournament uint             `json:"id_type_tournament" gorm:"not null;"`
	PlaceFrom        uint             `json:"place_from" gorm:"not null;"`
	PlaceTo          uint             `json:"place_to" gorm:"not null;"`
	NumberOfPoints   uint             `json:"number_of_points" gorm:"not null;"`
	School           School           `json:"school" gorm:"foreignkey:IDSportSchool"`
	TypeTournament   TypeOfTournament `json:"type_tournament" gorm:"foreignkey:IDTypeTournament"`
}

func (item *InfoScoreScale) Validate() (map[string]interface{}, bool) {
	//if item.Name == "" {
	//	return u.Message(false, "Coach name should be on the payload"), false
	//}

	return u.Message(true, "success"), true
}

func (item *InfoScoreScale) CreateInfoScoreScale() map[string]interface{} {
	resp, ok := item.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(item)
	resp["info_score_scale"] = item
	return resp
}

func UpdateInfoScoreScale(id string, newItem InfoScoreScale) *InfoScoreScale {
	item := &InfoScoreScale{}
	err := GetDB().Table("info_score_scales").Where("id = ?", id).First(item).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	item.Period = newItem.Period
	item.IDSportSchool = newItem.IDSportSchool
	item.TypeTournament = newItem.TypeTournament
	item.PlaceFrom = newItem.PlaceFrom
	item.PlaceTo = newItem.PlaceTo
	item.NumberOfPoints = newItem.NumberOfPoints

	GetDB().Save(item)
	return item

}

func GetInfoScoreScale(id string) *InfoScoreScale {
	item := &InfoScoreScale{}
	err := GetDB().Table("info_score_scales").Preload("School").Preload("TypeTournament").Where("id = ?", id).First(item).Error
	if err != nil {
		return nil
	}
	return item
}

func DeleteInfoScoreScale(id string) map[string]interface{} {

	db.Delete(&InfoScoreScale{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetInfoScoreScales() []*InfoScoreScale {
	items := make([]*InfoScoreScale, 0)
	dataBase := GetDB()
	err := dataBase.Table("info_score_scales").Preload("School").Preload("TypeTournament").Find(&items).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return items
}
