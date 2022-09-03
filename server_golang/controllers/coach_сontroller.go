package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateCoach(w http.ResponseWriter, r *http.Request) {
	item := &models.Coach{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateCoach()
	u.Respond(w, resp)
}

func UpdateCoach(w http.ResponseWriter, r *http.Request) {

	newItem := &models.Coach{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateCoach(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetСoaches(w http.ResponseWriter, r *http.Request) {
	data := models.GetСoaches()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteCoach(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteCoach(id)
	u.Respond(w, resp)
}

func GetCoach(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetCoach(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
