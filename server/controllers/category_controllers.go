package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"
	"net/http"
)

func CreateCategory(w http.ResponseWriter, r *http.Request) {
	category := &models.Category{}
	err := json.NewDecoder(r.Body).Decode(category)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := category.Create()
	u.Respond(w, resp)
}

func GetСategories(w http.ResponseWriter, r *http.Request) {
	data := models.GetCategorys()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
