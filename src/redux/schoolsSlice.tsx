import { createSlice, PayloadAction } from '@reduxjs/toolkit'

export interface School {
  id: string
  name: string
  adress: string
}

export interface AppState {
  value: School[]
}

const initialState: AppState = {
  value: [
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

  ],
}

export const appSlice = createSlice({
  name: 'counter',
  initialState,
  reducers: {
    /*
    increment: (state) => {
      // Redux Toolkit allows us to write "mutating" logic in reducers. It
      // doesn't actually mutate the state because it uses the Immer library,
      // which detects changes to a "draft state" and produces a brand new
      // immutable state based off those changes
      state.value += 1
    },
    decrement: (state) => {
      state.value -= 1
    },
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload
    },
    */
  },
})

export const {} = appSlice.actions
export default appSlice.reducer