import { configureStore } from "@reduxjs/toolkit";
import authSlice from "./auth/authSlice";

export const store = configureStore({
   reducer: {
      auth: authSlice,
   },
   // devTools: process.env.NODE_ENV === 'development',
   // middleware: (getDefaultMiddleware) => getDefaultMiddleware({}).concat([]),
})

export type RootState = ReturnType<typeof store.getState>
export type AppDispatch = typeof store.dispatch