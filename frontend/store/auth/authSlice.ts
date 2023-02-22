import { createSlice } from '@reduxjs/toolkit'
import type { PayloadAction } from '@reduxjs/toolkit'
import { AuthState } from './types'
import { authUser } from '@/services'
import jwt_decode from 'jwt-decode'

// const token = localStorage.getItem('access_token') ? localStorage.getItem('access_token') : null

const initialState: AuthState = {
   token: null,
   is_authenticated: false,
   user: null,
   error: null,
   success: false
}

const authSlice = createSlice({
   name: 'auth',
   initialState,
   reducers: {
      loginuser: (state, action) => {
         authUser(action.payload)
         .then(res => {
            if (res.access && res.refresh) {
               state.token = res.access
               state.success = true
            }
            else {
               state.error = res.statusText
            }
         })
      }
   },
})

export const {loginuser, } = authSlice.actions

export const selectToken = state => state.auth.token

export default authSlice.reducer