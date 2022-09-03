package models

import (
	u "first-line/utils"
	"fmt"

	"github.com/jinzhu/gorm"
)

type School struct {
	gorm.Model
	Name   string `json:"name" gorm:"not null"`
	Adress string `json:"adress"`
}

func (school *School) Validate() (map[string]interface{}, bool) {
	if school.Name == "" {
		return u.Message(false, "School name should be on the payload"), false
	}

	return u.Message(true, "success"), true
}

func (school *School) CreateSchool() map[string]interface{} {
	resp, ok := school.Validate()
	if !ok {
		return resp
	}

	GetDB().Create(school)
	resp["school"] = school
	return resp
}

func UpdateSchool(id string, newSchool School) *School {
	school := &School{}
	err := GetDB().Table("schools").Where("id = ?", id).First(school).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	school.Adress = newSchool.Adress
	school.Name = newSchool.Name
	GetDB().Save(school)
	return school

}

func GetSchool(id string) *School {
	school := &School{}
	err := GetDB().Table("schools").Where("id = ?", id).First(school).Error
	if err != nil {
		return nil
	}
	return school
}

func DeleteSchool(id string) map[string]interface{} {

	db.Delete(&School{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetSchools(name string, address string) []*School {
	fmt.Println(name)
	fmt.Println(address)

	school := make([]*School, 0)
	var err error
	if name != "" && address != "" {
		err = GetDB().Table("schools").Where("name LIKE", name).Where("address LIKE", address).Find(&school).Error
	} else if name != "" && address == "" {
		err = GetDB().Table("schools").Where("name LIKE", name).Find(&school).Error
	} else {
		err = GetDB().Table("schools").Find(&school).Error
	}
	//err := GetDB().Table("schools").Find(&school).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return school
}
