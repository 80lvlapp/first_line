export interface School {
    id: string
    name: string
    adress: string
  }

export interface Raiting {
  sportsman: Sportsman
  place: number
  points: number
  сhangingPosition: number
}
  
export interface Sportsman {

  id: string
  name: string

}