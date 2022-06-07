package controllers

import (
	"encoding/json"
	"first-line/models"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateInfoScoreScale(w http.ResponseWriter, r *http.Request) {
	item := &models.InfoScoreScale{}
	err := json.NewDecoder(r.Body).Decode(item)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := item.CreateInfoScoreScale()
	u.Respond(w, resp)
}

func UpdateInfoScoreScale(w http.ResponseWriter, r *http.Request) {

	newItem := &models.InfoScoreScale{}
	err := json.NewDecoder(r.Body).Decode(newItem)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.UpdateInfoScoreScale(id, *newItem)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetInfoScoreScales(w http.ResponseWriter, r *http.Request) {
	data := models.GetInfoScoreScales()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteInfoScoreScale(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := models.DeleteInfoScoreScale(id)
	u.Respond(w, resp)
}

func GetInfoScoreScale(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := models.GetInfoSportsman(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
