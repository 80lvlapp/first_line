package school

import (
	"encoding/json"
	u "first-line/utils"

	"net/http"

	"github.com/gorilla/mux"
)

func CreateSchool(w http.ResponseWriter, r *http.Request) {
	school := &School{}
	err := json.NewDecoder(r.Body).Decode(school)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	resp := school.CreateSchool()
	u.Respond(w, resp)
}

func UpdateSchool(w http.ResponseWriter, r *http.Request) {

	newSchool := &School{}
	err := json.NewDecoder(r.Body).Decode(newSchool)
	if err != nil {
		u.Respond(w, u.Message(false, "Error while decoding request body"))
		return
	}
	vars := mux.Vars(r)
	id := vars["id"]
	data := UpdateSchoolDb(id, *newSchool)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)

}

func GetSchools(w http.ResponseWriter, r *http.Request) {
	data := GetSchoolsDb()
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}

func DeleteSchool(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	resp := DeleteSchoolDb(id)
	u.Respond(w, resp)
}

func GetSchool(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	id := vars["id"]
	data := GetSchoolDb(id)
	resp := u.Message(true, "success")
	resp["data"] = data
	u.Respond(w, resp)
}
