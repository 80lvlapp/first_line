import { configureStore } from '@reduxjs/toolkit'
import appSlice from '../redux/appSlice'
import auth from '../redux/authSlice'


import { api } from './apiSlice'

export const store = configureStore({
  reducer: {
    app: appSlice,
    auth,
    [api.reducerPath]: api.reducer,
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch