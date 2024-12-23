# src/my_project/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, SerperDevTool


@CrewBase
class NoteEvalCrew():
    """Note Eval Crew"""

    @agent
    def note_summarizer(self) -> Agent:
        # file_read_tool = FileReadTool(file_path='my_note.txt')
        return Agent(
            config=self.agents_config['note_summarizer'],
            verbose=True,
            tools=[FileReadTool('my_note.txt')],
            
        )


    @agent
    def note_complementer(self) -> Agent:
       
        return Agent(
            config=self.agents_config['note_complementer'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def learning_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['learning_advisor'],
            verbose=True
        )

    @task
    def note_summarization_task(self) -> Task:
        return Task(
            config=self.tasks_config['note_summarization_task'],
            output_file='note_summary.md'
        )

    @task
    def note_complementation_task(self) -> Task:
        return Task(
            config=self.tasks_config['note_complementation_task'],
            output_file='note_comparison.md'
        )

    @task
    def learning_advice_task(self) -> Task:
        return Task(
            config=self.tasks_config['learning_advice_task'],
            output_file='note_next_steps.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Note Eval Crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )