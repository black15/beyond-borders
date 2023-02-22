export interface IUser {
	email: string,
   exp: number,
   iat: number,
   jti: string,
   token_type: string,
   user_id: number,
   user_type: number,
   username: string,
}

export interface AuthState {
   token: string | null,
   is_authenticated: boolean,
   user: IUser | null,
   error: string | null,
   success: boolean
}