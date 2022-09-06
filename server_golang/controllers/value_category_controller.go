package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateValueCategory(w http.ResponseWriter, r *http.Request) {
	item := &models.ValueCategory{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateValueCategory()
	u.Respond(w, resp)
}

func UpdateValueCategory(w http.ResponseWriter, r *http.Request) {

	newItem := &models.ValueCategory{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateValueCategory(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetValueCategores(w http.ResponseWriter, r *http.Request) {
	data := models.GetValueCategorys()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteValueCategory(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteValueCategory(id)
	u.Respond(w, resp)
}

func GetValueCategory(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetValueCategory(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
