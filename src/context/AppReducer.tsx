
import {Action, State, ActionType} from "./stateType";

// Создаём редьюсер, принимающий на вход текущий стейт и объект Action с полями type и payload, тип возвращаемого редьюсером значения - State
export const AppReducer = (state: State, action: Action):State => {
    switch (action.type) {
        // case ActionType.ADD: {
        //     return {...state, schools: [...state.schools, {
        //             name: action.payload,
        //             adress: "",
        //             id: ""
        //         }]}
        case ActionType.ADD: {
                return {...state, schools: action.payload}
        }
        case ActionType.CHANGE: {
            return {...state, stringParam: action.payload}
        }
        // case ActionType.REMOVE: {
        //     return {...state, schools:  [...state.schools.filter(item => item !== action.payload)]}
        // }
        // case ActionType.TOGGLE: {
        //     return {...state, schools: [...state.schools.map((item) => (item !== action.payload ? item : {...item, adress: ""}))]}
        // }
        default: throw new Error('Unexpected action');
    }
};