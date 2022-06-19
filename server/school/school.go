package school

import (
	u "first-line/utils"
	"fmt"

	db "first-line/models"
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

	db.GetDB().Create(school)
	resp["school"] = school
	return resp
}

func UpdateSchoolDb(id string, newSchool School) *School {
	school := &School{}
	err := db.GetDB().Table("schools").Where("id = ?", id).First(school).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}

	school.Adress = newSchool.Adress
	school.Name = newSchool.Name
	db.GetDB().Save(school)
	return school

}

func GetSchoolDb(id string) *School {
	school := &School{}
	err := db.GetDB().Table("schools").Where("id = ?", id).First(school).Error
	if err != nil {
		return nil
	}
	return school
}

func DeleteSchoolDb(id string) map[string]interface{} {

	db.GetDB().Delete(&School{}, id)
	resp := u.Message(true, "success")
	return resp

}

func GetSchoolsDb() []*School {
	school := make([]*School, 0)
	err := db.GetDB().Table("schools").Find(&school).Error
	if err != nil {
		fmt.Println(err)
		return nil
	}
	return school
}
