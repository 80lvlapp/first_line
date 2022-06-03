package models

import (
	"fmt"
	"github.com/jinzhu/gorm"
	u "first-line/utils"
)

type School struct {
	gorm.Model
	Name           string `json:"name"`
	Adress         string `json:"adress"`
}

func (category *School) Validate() (map[string]interface{}, bool) {
	if category.Name == "" {
		return u.Message(false, "School name should be on the payload"), false
	}
	return u.Message(true, "success"), true
}

func (school *School) CreateSchool() map[string]interface{} {
	if resp, ok := school.Validate(); !ok {
		return resp
	}
	GetDB().Create(school)
	resp := u.Message(true, "success")
	resp["school"] = school
	return resp
}

func (school *School) UpdateSchool() map[string]interface{} {
	if resp, ok := school.Validate(); !ok {
		return resp
	}
	GetDB().Update(school)
	resp := u.Message(true, "success")
	resp["school"] = school
	return resp
}

func GetSchool(id string) *School {
	school := &School{}
	err := GetDB().Table("schools").Where("id = ?", id).First(school).Error
	if err != nil {
		return nil
	}
	return school
}

func DeleteSchool(id string)  map[string]interface{}{
	
	db.Delete(&School{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetSchools() []*School {
	school := make([]*School, 0)
	err := GetDB().Table("schools").Find(&school).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return school
}
