import { createSlice, PayloadAction} from '@reduxjs/toolkit'
import { RootState } from "./store";

export interface AuthError {
    message: string
}

export interface AuthState {
    isAuth: boolean
    currentUser?: CurrentUser
    isLoading: boolean
    error: AuthError
}

export interface CurrentUser {
    id: string
    display_name: string
    email: string
    photo_url: string
}

export const initialState: AuthState = {
    isAuth: false,
    isLoading: false,
    error: {message: 'An Error occurred'},
    currentUser: undefined
}

export const authSlice = createSlice({
    name: 'auth',
    initialState,
    reducers: {
        setLoading: (state, {payload}: PayloadAction<boolean> ) => {
            state.isLoading = payload
        },
        setAuthSuccess: (state, { payload }: PayloadAction <CurrentUser>) => {
            state.currentUser = payload;
            state.isAuth = true
        },
        setLogOut: (state) => {
            state.isAuth = false
            state.currentUser = undefined
        },
        setAuthFailed: (state, { payload }: PayloadAction <AuthError>) => {
           state.error = payload;
            state.isAuth = false
        },
    },
})

export default authSlice.reducer;
export const { setAuthSuccess, setLogOut, setLoading, setAuthFailed} = authSlice.actions
export const selectCurrentUser = (state: RootState) => state.auth.currentUser;