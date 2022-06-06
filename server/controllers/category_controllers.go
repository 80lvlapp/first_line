package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"
	"github.com/gorilla/mux"
	"net/http"
)

func CreateCategory(w http.ResponseWriter, r *http.Request) {
	item := &models.Category{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateCategory()
	u.Respond(w, resp)
}

func UpdateCategory(w http.ResponseWriter, r *http.Request) {

	newItem := &models.Category{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateCategory(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetCategories(w http.ResponseWriter, r *http.Request) {
	data := models.GetCategorys()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteCategory(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteCategory(id)
	u.Respond(w, resp)
}

func GetCategory(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetCategory(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
