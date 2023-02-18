import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'
import Cookies from 'js-cookie'

export interface AuthState {
   token: string | null,
   is_authenticated: boolean,
   user: {username: string | null},
   error: string | null,
   success: boolean
}

const initialState: AuthState = {
   token: null,
   is_authenticated: false,
   user: {username: null},
   error: null,
   success: false
}

const authSlice = createSlice({
   name: 'auth',
   initialState,
   reducers: {}
})

export default authSlice.reducer