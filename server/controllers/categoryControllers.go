package controllers

import (
	"encoding/json"
	"go-contacts/models"
	u "go-contacts/utils"
	"net/http"
)

var CreateCategory = func(w http.ResponseWriter, r *http.Request) {
	category := &models.Category{}
	err := json.NewDecoder(r.Body).Decode(category)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := category.Create()
	u.Respond(w, resp)
}

var GetСategories = func(w http.ResponseWriter, r *http.Request) {
	data := models.GetCategorys()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
