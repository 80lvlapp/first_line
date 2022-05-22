import { createContext, useContext } from "react";
import { ContextState } from "./stateType";
// export const AppContext = createContext<Partial<ContextState>>({});
export const AppContext = createContext<ContextState | undefined>(undefined);

export const useAppContext = (): ContextState => {
  const context = useContext(AppContext)
  if (!context) {
    throw Error('use Provider')
  }
  return context
}
