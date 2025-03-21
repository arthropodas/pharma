export type RegisterRequest = {
    firstName: string;
    lastName?: string; 
    gender:number;
    dob: string | null; 
    email: string; 
    phoneNumber?: string | null; 
    userType: number
    password: string;
    // profileImage?: File | null; 
  };
  
export type LoginRequest={
  username: string;
  password: string
}