package controllers

import (
	"encoding/json"
	"go-contacts/models"
	u "go-contacts/utils"
	"net/http"
)

var CreateInspectionGroup = func(w http.ResponseWriter, r *http.Request) {

	user := r.Context().Value("user").(uint) //Grab the id of the user that send the request
	inspectionGroup := &models.InspectionGroup{}
	err := json.NewDecoder(r.Body).Decode(inspectionGroup)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	inspectionGroup.UserId = user
	resp := inspectionGroup.Create()
	u.Respond(w, resp)
}

var GetInspectionGroupsFor = func(w http.ResponseWriter, r *http.Request) {

	id := r.Context().Value("user").(uint)
	data := models.GetInspectionGroups(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
