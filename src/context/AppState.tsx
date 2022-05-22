import React, { useReducer } from "react";
import { AppContext } from "./AppContext";
import { Action, ActionType, State, ContextState } from "./stateType";
import { AppReducer } from "./AppReducer";

type Props = {
  children?: React.ReactNode;
};

export const AppState: React.FC<Props> = ({ children }) => {
  // Начальные значения стейта
  const initialState: State = {
    stringParam: "",
    schools: [],
  };

  const [state, changeState] = useReducer<React.Reducer<State, Action>>(
    AppReducer,
    initialState
  );

  const testChangeState = (param: string) => {
    changeState({ type: ActionType.CHANGE, payload: param });
  };

  const getSportsSchools = () => {

    changeState({ type: ActionType.ADD, payload: [
      {
       name: "Тацудзин каратэ",
       id: "1",
       adress: "г. Лобня"
      },
      {
        name: "Клую Союз",
        id: "2",
        adress: "г. Электросталь"
       }
    ] });

  }

  const ContextState: ContextState = {
    state,
    changeState,
    testChangeState,
    getSportsSchools,
  };

  return (
    <>
      <AppContext.Provider value={ContextState}>{children}</AppContext.Provider>
    </>
  );
};
