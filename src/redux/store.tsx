import { configureStore } from '@reduxjs/toolkit'
import appSlice from '../redux/appSlice'


import { api } from './apiSlice'

export const store = configureStore({
  reducer: {
    app: appSlice,
    [api.reducerPath]: api.reducer,
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch