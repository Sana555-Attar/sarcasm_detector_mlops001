from clearml.automation import TriggerScheduler

trigger=TriggerScheduler(pooling_frequency_minutes=0.1)

trigger.add_dataset_trigger(name='Retrain on Dataset',
                            schedule_task_id='80bf2d5710c444a7bed93d780e7e5db4',
                            schedule_queue='default',
                            trigger_project='sarcasm_detector',
                            trigger_name='sarcasm_dataset')

#trigger.start()

trigger.start_remotely()