import pandas as pd

class CollegeInfoBot:
    def __init__(self, excel_file):
        # Load the Excel file
        self.df = pd.read_excel(excel_file)

    def get_college_info(self, college_name):
        # Find the college in the DataFrame
        college_info = self.df[self.df['Institution'].str.contains(college_name, case=False, na=False)]
        
        if college_info.empty:
            return f"No information found for {college_name}."
        
        # Assuming we want to show specific columns
        info = college_info.iloc[0]
        return {
            'Institution': info['Institution'],
            'State': info['State'],
            'Region': info['Region'],
            'Aid Policy': info['Aid Policy'],
            'Total Cost': info['Total Cost of Attendance (out-of- state) (1)'],
            'Full-Time Undergrads': info['Full-Time Undergrads'],
            'Full-Time International Undergrads': info['Full-Time International Undergrads'],
            'Percentage of Internationals to All Undergrads': info['Percentage of Internationals to All Undergrads']*100,
            'Average International Noncitizen Financial Aid Award': info['Average International Noncitizen Financial Aid Award'],
            'Percentage of International Noncitizens Receiving Aid (3)': info['Percentage of International Noncitizens Receiving Aid (3)']*100
        }

# Example usage
if __name__ == "__main__":
    # Initialize the bot with the path to your Excel file
    bot = CollegeInfoBot('colleges.xlsx')

    # Query information about a specific college
    college_name = input("Enter the college name: ")
    info = bot.get_college_info(college_name)
    
    if isinstance(info, dict):
        print(f"Information for {info['Institution']}:")
        for key, value in info.items():
            print(f"{key}: {value}")
    else:
        print(info)
