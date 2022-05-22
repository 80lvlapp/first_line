import { configureStore } from '@reduxjs/toolkit'
import appSlice from '../redux/appSlice'
import auth from '../redux/authSlice'
import schools from '../redux/schoolsSlice'




export const store = configureStore({
  reducer: {
    app: appSlice,
    auth,
    schools
  }
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch