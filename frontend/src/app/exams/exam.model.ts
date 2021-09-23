export class Exam {
  constructor(
    public title: string,
    public description: string,
    public _id?: number,
    public updatedAt?: Date,
    public createdAt?: Date,
    public lastUpdatedBy?: string,
  ) { }
}

export class Teste {
  constructor(
    public title: string
  ) {
  }
}
