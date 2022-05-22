import { Dispatch } from "react";

// Созданная задача имеет название и статус готовности
export type School = {
  name: string;
  id: string;
  adress: string;
};

export type Schools = School[];

// В состоянии хранится записываемая в инпут новая задача, а также массив уже созданных задач
export type State = {
  stringParam: string;
  schools: Schools;
};

// Все возможные варианты действий со стейтом
export enum ActionType {
  ADD = "ADD",
  CHANGE = "CHANGE",
  REMOVE = "REMOVE",
  TOGGLE = "TOGGLE",
}

// Для действий ADD и CHANGE доступна передача только строковых значений
type ActionStringPayload = {
  type: ActionType.CHANGE;
  payload: string;
};

// Для действий TOGGLE и REMOVE доступна передача только объекта типа Task
type ActionObjectPayload = {
  //type: ActionType.TOGGLE | ActionType.REMOVE | ActionType.ADD;
  type: ActionType.ADD;
  payload: Schools;
};

// Объединяем предыдущие две группы для использования в редьюсере
export type Action = ActionStringPayload | ActionObjectPayload;

// Наш контекст состоит из стейта и функции-редьюсера, в которую будут передаваться Action. Тип Dispatch импортируется из библиотеки react
export type ContextState = {
  state: State;
  changeState: Dispatch<Action>;
  testChangeState: (param: string) => void;
  getSportsSchools: () => void;
};
