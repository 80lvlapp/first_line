package models

import (
	"fmt"
	"github.com/jinzhu/gorm"
	u "first-line/utils"
)

type InspectionGroup struct {
	gorm.Model
	Name   string `json:"name"`
	UserId uint   `json:"user_id"` //The user that this contact belongs to
}

/*
 This struct function validate the required parameters sent through the http request body

returns message and true if the requirement is met
*/
func (inspectionGroup *InspectionGroup) Validate() (map[string]interface{}, bool) {

	if inspectionGroup.Name == "" {
		return u.Message(false, "Contact name should be on the payload"), false
	}

	
	if inspectionGroup.UserId <= 0 {
		return u.Message(false, "User is not recognized"), false
	}

	//All the required parameters are present
	return u.Message(true, "success"), true
}

func (inspectionGroup *InspectionGroup) Create() (map[string]interface{}) {

	if resp, ok := inspectionGroup.Validate(); !ok {
		return resp
	}

	GetDB().Create(inspectionGroup)

	resp := u.Message(true, "success")
	resp["inspectionGroup"] = inspectionGroup
	return resp
}

func GetInspectionGroup(id uint) (*InspectionGroup) {

	inspectionGroup := &InspectionGroup{}
	err := GetDB().Table("inspection_groups").Where("id = ?", id).First(inspectionGroup).Error
	if err != nil {
		return nil
	}
	return inspectionGroup
}

func GetInspectionGroups(user uint) ([]*InspectionGroup) {

	inspectionGroup := make([]*InspectionGroup, 0)
	err := GetDB().Table("inspection_groups").Where("user_id = ?", user).Find(&inspectionGroup).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	return inspectionGroup
}
