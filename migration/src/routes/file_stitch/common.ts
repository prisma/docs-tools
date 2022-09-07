export interface BodyPart {
    index: number;
    key: string;
}

export interface FilePath { 
    new_path: string;
    name?: string;
    header: [string, string][];
    body: BodyPart[];
};