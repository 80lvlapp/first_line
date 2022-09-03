package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"
	"fmt"
	"net/http"

	"github.com/gorilla/mux"
)

func CreateSchool(w http.ResponseWriter, r *http.Request) {
	school := &models.School{}
	err := json.NewDecoder(r.Body).Decode(school)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := school.CreateSchool()
	u.Respond(w, resp)
}

func UpdateSchool(w http.ResponseWriter, r *http.Request) {

	newSchool := &models.School{}
	err := json.NewDecoder(r.Body).Decode(newSchool)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateSchool(id, *newSchool)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetSchools(w http.ResponseWriter, r *http.Request) {
	queries := mux.Vars(r)
	fmt.Println(queries)
	data := models.GetSchools("", "")
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func GetSchoolsLikeName(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	name := vars["name"]
	fmt.Println(name)
	data := models.GetSchools(name, "")
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteSchool(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteSchool(id)
	u.Respond(w, resp)
}

func GetSchool(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetSchool(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
