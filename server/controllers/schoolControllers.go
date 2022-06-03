package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"
	"net/http"
	"github.com/gorilla/mux"
)

var CreateSchool = func(w http.ResponseWriter, r *http.Request) {
	school := &models.School{}
	err := json.NewDecoder(r.Body).Decode(school)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := school.CreateSchool()
	u.Respond(w, resp)
}

var UpdateSchool = func(w http.ResponseWriter, r *http.Request) {
	school := &models.School{}
	err := json.NewDecoder(r.Body).Decode(school)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := school.UpdateSchool()
	u.Respond(w, resp)
}

var GetSchools = func(w http.ResponseWriter, r *http.Request) {

	data := models.GetSchools();
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

var DeleteSchool = func(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteSchool(id);
	u.Respond(w, resp)
}

var GetSchool = func(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetSchool(id);
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

